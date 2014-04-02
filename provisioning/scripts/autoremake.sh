#!/bin/sh

CFG_INVENIO_SRCDIR=${CFG_INVENIO_SRCDIR:=/home/invenio/invenio}
CFG_INVENIO_PREFIX=${CFG_INVENIO_PREFIX:=/opt/invenio}

cd "$CFG_INVENIO_SRCDIR" && aclocal && automake -a && autoconf && ./configure \
   --prefix="$CFG_INVENIO_PREFIX"  \
   --with-libintl-prefix=/opt/local
