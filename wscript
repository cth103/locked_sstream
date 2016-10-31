#
#    Copyright (C) 2016 Carl Hetherington <cth@carlh.net>
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

APPNAME = 'locked_sstream'
VERSION = '0.0.4devel'

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
