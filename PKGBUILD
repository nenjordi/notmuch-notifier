# Maintainer: Jordi <nenjordi@JORDI-LENOVO>
pkgname=notmuch-notifier
pkgver=0.1
pkgrel=1
epoch=
pkgdesc="Python script to get libnotify notifications fed from a notmuch filter"
arch=('i686' 'x86_64')
url="https://github.com/nenjordi/notmuch-notifier"
license=('GPL')
groups=()
depends=('python' 'notmuch')
makedepends=('git')
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=notmuch-notifier.install
changelog=
source=("git+https://github.com/nenjordi/notmuch-notifier.git")
md5sums=('SKIP')
noextract=()

prepare() {
  cd "$srcdir/$pkgname"
}

build() {
  cd "$srcdir/$pkgname"

}

check() {
  cd "$srcdir/$pkgname"

  # check if python-notify2 is installed
}

package() {
  cd "$srcdir/$pkgname"
  mkdir -p "$pkgdir/usr/local/bin/"
  cp "$srcdir/$pkgname/notmuch-notifier.py" "$pkgdir/usr/local/bin/"

  # doc
  mkdir -p "$pkgdir/usr/local/share/doc/$pkgname/"
  cp "$srcdir/$pkgname/notmuch-notifier.conf" "$pkgdir/usr/local/share/doc/$pkgname/"
  cp "$srcdir/$pkgname/Readme.md" "$pkgdir/usr/local/share/doc/$pkgname/"
}

# vim:set ts=2 sw=2 et:
