## different tests behaviour depending on TESTS_SUCCESS variable

TESTS_SUCCESS behaviour
- `always` all tests are passing
- `never` all tests are  (FAILED)
- `broken` fixture throws exception (BROKEN)
- `random` or not set – 10-20% probability of failure in asserts

```shell
export TESTS_SUCCESS=random; ./runallure3.sh
export TESTS_SUCCESS=always; ./runallure3.sh
export TESTS_SUCCESS=broken; ./runallure3.sh
export TESTS_SUCCESS=always; ./runtests.sh 276
export TESTS_SUCCESS=random; ./runtests.sh
export TESTS_SUCCESS=broken; ./runtests.sh




export TESTS_SUCCESS=always; ./runtests.sh 276
export TESTS_SUCCESS=never; ./runtests.sh 276

```