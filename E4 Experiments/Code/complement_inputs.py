"""Strict complement inputs used by E4; embedded in both standalone notebooks.

Native masks and standardized raw caches are external licensed assets. This
module does not fit anatomy, resize cached raw images or select new subjects.
"""
import json
from pathlib import Path

import cv2
import numpy as np
import pandas as pd
import torch

NORMALIZATION = {'mean': 0.48287347719744544, 'std': 0.2741831329802273}


def native_footprint(support, geometry):
    size = geometry['content_width'], geometry['content_height']
    fraction = support.astype('float32')
    if fraction.shape != (size[1], size[0]):
        fraction = cv2.resize(fraction, size, interpolation=cv2.INTER_AREA)
    return cv2.copyMakeBorder(fraction, geometry['pad_top'], geometry['pad_bottom'],
        geometry['pad_left'], geometry['pad_right'], cv2.BORDER_CONSTANT, value=0)


def content_mask(geometry):
    result = np.zeros((320, 320), bool)
    y, x = geometry['pad_top'], geometry['pad_left']
    result[y:y+geometry['content_height'], x:x+geometry['content_width']] = True
    return result


def removal_mask(native_annulus, geometry, original_annulus):
    if native_annulus.dtype != np.bool_:
        raise ValueError('Expected native Boolean annulus')
    fraction = native_footprint(native_annulus, geometry)
    removal = original_annulus | (fraction > 0)
    content = content_mask(geometry)
    if removal.shape != (320, 320) or np.any(removal & ~content):
        raise ValueError('Removal crosses original image geometry')
    if np.any((fraction > 0) & ~removal):
        raise ValueError('Native annulus sampling contribution remains')
    return removal, fraction


def mean_fill(normalized, mask, content):
    assert normalized.dtype == torch.float32 and normalized.shape == (1, 320, 320)
    assert mask.dtype == np.bool_ and not (mask & ~content).any()
    output = normalized.clone()
    selection = torch.from_numpy(mask)
    output[:, selection] = 0.
    assert torch.equal(output[:, ~selection], normalized[:, ~selection])
    return output


def tensor_from_pixels(pixels, mask, content, augmentation=None):
    if pixels.dtype != np.uint8 or pixels.shape != (320, 320):
        raise ValueError('Use original standardized grayscale cache; no resize')
    image = torch.from_numpy(np.ascontiguousarray(pixels[None])).float().div(255)
    if augmentation is not None:
        # Discard texture before contrast computes the image mean.
        image[:, torch.from_numpy(mask)] = NORMALIZATION['mean']
        image = augmentation(image)
    normalized = (image-NORMALIZATION['mean'])/NORMALIZATION['std']
    return mean_fill(normalized, mask, content)


def attach_removal_masks(records, manifest, mask_root, path_remap=None):
    """Join the frozen train/validation mask asset without changing membership."""
    table = pd.read_parquet(manifest)
    if not table.image_id.is_unique:
        raise ValueError('Duplicate image in complement mask manifest')
    active = [r for r in records if r['split'] in ('train', 'validation')]
    if set(table.image_id) != {r['image_id'] for r in active}:
        raise ValueError('Complement manifest must match frozen train/validation exactly')
    by_id = table.set_index('image_id').to_dict('index')
    result = []
    for record in records:
        row = dict(record)
        if row['split'] in ('train', 'validation'):
            selected = by_id[row['image_id']]
            if 'split' in selected and selected['split'] != row['split']:
                raise ValueError('Complement mask split mismatch')
            value = str(selected['removal_mask_path']).replace('\\', '/')
            for old, new in sorted((path_remap or {}).items(), key=lambda p:-len(str(p[0]))):
                prefix = str(old).replace('\\', '/').rstrip('/')
                if value == prefix or value.startswith(prefix+'/'):
                    value = str(Path(new)/value[len(prefix):].lstrip('/'))
                    break
            path = Path(value)
            row['e4_removal_mask_path'] = (path if path.is_absolute() else Path(mask_root)/path).resolve()
        result.append(row)
    return result
