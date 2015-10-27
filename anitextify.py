#!/usr/bin/env python
#
# Copyright 2015 Jonathan Vollebregt <jnvsor@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from gimpfu import *

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)

def anitextify(i, l, direction=(0, 1), delay=30):
    out = gimp.Image(i.width, i.height, 0)
    layer = gimp.pdb.gimp_layer_new_from_visible(i, out, "Base") # TODO: Use python bindings
    l = layer

    if direction[0]:
        size = out.width
    else:
        size = out.height

    for n in range(size):
        l = gimp.pdb.gimp_layer_new_from_drawable(l, out) # TODO: Use python bindings
        l.name = "Frame {} ({}ms)".format(n + 1, delay)
        out.add_layer(l, -1)
        l.offset(True, 0, direction[0], direction[1])

    del layer
    gimp.Display(out)

register(
    "anitextify",
    N_("Apply a simple scrolling animation to a texture"),
    """Creates an simple scrolling animation from a layer""",
    "Jonathan Vollebregt",
    "Copyright Jonathan Vollebregt GPL v3.0",
    "2015",
    _("Ani_textify.."),
    "*",
    [
        (PF_IMAGE, "i", "Input image", None),
        (PF_DRAWABLE, "l", "Input drawable", None), # TODO: Get rid of this somehow, we don't need it
        (PF_RADIO, "direction", _("Direction"), (0, 1), (
            ("Down", (0, 1)),
            ("Right", (1, 0)),
            ("Up", (0, -1)),
            ("Left", (-1, 0))
        )),
        (PF_INT, "delay", _("Delay between frames"), 30),
    ],
    [],
    anitextify,
    menu="<Image>/Filters/Animation",
    domain=("gimp20-python", gimp.locale_directory)
)

main()
