"""No op resizer"""
from r2.lib.providers.image_resizing import ImageResizingProvider


class NoOp2ImageResizingProvider(ImageResizingProvider):
    """A passthrough solution that won't actually resize any images.

    Combines well with the filesystem media provider for an entirely local
    setup.
    """
    def resize_image(self, image, width=None, censor_nsfw=False, max_ratio=None, file_type=None):
        # The simplest solution: just pass it on through.
        return image['url']
