#
#    Copyright (C) 2016-2018 Carl Hetherington <cth@carlh.net>
#
#    This file is part of locked_sstream.
#
#    locked_sstream is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    locked_sstream is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with locked_sstream.  If not, see <http://www.gnu.org/licenses/>.
#

import subprocess
import shlex

APPNAME = 'locked_sstream'

this_version = subprocess.Popen(shlex.split('git tag -l --points-at HEAD'), stdout=subprocess.PIPE).communicate()[0]
last_version = subprocess.Popen(shlex.split('git describe --tags --abbrev=0'), stdout=subprocess.PIPE).communicate()[0]

if isinstance(this_version, bytes):
    this_version = this_version.decode('UTF-8')
if isinstance(last_version, bytes):
    last_version = last_version.decode('UTF-8')

if this_version == '':
    VERSION = '%sdevel' % last_version[1:].strip()
else:
    VERSION = this_version[1:].strip()

def configure(conf):
    pass

def build(bld):

    bld(source='locked_sstream.pc.in' % bld.env.API_VERSION,
        version=VERSION,
        includedir='%s/include' % bld.env.PREFIX,
        install_path='${LIBDIR}/pkgconfig')

    bld.install_files('${PREFIX}/include', 'locked_sstream.h')

def dist(ctx):
    ctx.excl = 'TODO core *~ .git build .waf* .lock* doc/*~ src/*~  __pycache__ GPATH GRTAGS GSYMS GTAGS'
