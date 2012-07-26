#Image Detective

##Description

**ImageDetective** is a module which elaborates images. Now in module are implemented the methods listed here below:

* point_detection, is the method which detects image's isolated point.
* edge_detection, it detects image's edge.


##Dependency

* PIL
* cv

##Example

```python
import sys
import imagedetective

my_image = imagedetective.ImageDetective("original.jpg")
print "Edge detection is executing..."
my_image.edge_detection(40)
print "Done! Saving image..."
my_image.save_image("example.jpg", "JPEG")
print "Done!"
```


##License

### ImageDetective is released under the [GNU General Public License (GPL3)](https://www.gnu.org/licenses/gpl-3.0.html):
Copyright (C) 2012 EmanueleSgroi <emanuele.sgroi@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

On Debian systems, the complete text of the GNU General Public License
can be found in /usr/share/common-licenses/GPL-3.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
