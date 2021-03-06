# Copyright 1999-2003 Gentoo Technologies, Inc.
# Distributed under the terms of the GNU General Public License v2
# $Header: /home/cvsroot/gentoo-x86/dev-util/scons/scons-2.3.0.ebuild,v 1.2 2003/02/13 12:00:11 vapier Exp $

MY_P=${PN}-2.3.0
S=${WORKDIR}/${MY_P}
DESCRIPTION="Extensible python-based build utility"
SRC_URI="mirror://sourceforge/${PN}/${MY_P}.tar.gz"
HOMEPAGE="http://www.scons.org"

SLOT="0"
LICENSE="as-is"
KEYWORDS="~x86 ~sparc"

DEPEND=">=dev-lang/python-2.4"

src_compile() {
        python setup.py build
}

src_install () {
        python setup.py install --root=${D}
        dodoc *.txt PKG-INFO MANIFEST
        doman scons.1
        doman sconsign.1
}
