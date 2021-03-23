# -*- coding: utf-8 -*-
"""Compositing tests for use with pytest."""
import sys
from os.path import join

import pytest

from moviepy.editor import *
from moviepy.utils import close_all_clips

from .test_helper import TMP_DIR

def test_clips_array_duration():
    red = ColorClip((1024,800), color=(255,0,0))
    green = ColorClip((1024,800), color=(0,255,0))
    blue = ColorClip((1024,800), color=(0,0,255))

    with clips_array([[red, green, blue]]).set_duration(5) as video:
        with pytest.raises(AttributeError,
                           message="Expecting ValueError (fps not set)"):
             video.write_videofile(join(TMP_DIR, "test_clips_array.mp4"))

    video = clips_array([[red, green, blue]])

    #this one should work correctly
    red.fps = green.fps = blue.fps = 30

    with clips_array([[red, green, blue]]).set_duration(5) as video:
        video.write_videofile(join(TMP_DIR, "test_clips_array.mp4"))

    red.close()
    green.close()
    blue.close()
