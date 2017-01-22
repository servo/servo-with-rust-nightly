# Servo with Rust Nightly

Since Servo uses unstable Rust features,
updating the Rust compiler might introduce breaking changes to these features
and therefore prevent Servo from building or running correctly.
Sometimes, a compiler bug that affects Servo might be introduced.
To avoid dealing with this constantly, Servo pins to a specific version of Rust Nightly.

The flip side of pinning is that we are not aware of breakage or bugs
until we actively try to update the compiler.

In order to help find out about these sooner,
this repository makes Travis-CI build Servo daily with the latest Rust Nightly
(not the pinned version).
When the build fails, we get notified.

* Build configuration:
  [`.travis.yml`](https://github.com/servo/servo-with-rust-nightly/blob/master/.travis.yml)
* Latest build:
  [![Build Status](https://travis-ci.org/servo/servo-with-rust-nightly.svg?branch=master)](
  https://travis-ci.org/servo/servo-with-rust-nightly)
* To be improved: [better reporting on failure](https://github.com/servo/servo-with-rust-nightly/issues/1)
