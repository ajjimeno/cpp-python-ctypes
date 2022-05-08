g++ -c -fPIC foo.cpp -o foo.o
g++ -shared -W1,-soname,libfoo.so -o libfoo.so foo.o

g++ -c -fPIC runner.cpp -o test.o                    
g++ -shared -W1,-soname,libtest.so -o libtest.so test.o

g++ -c -fPIC factorial.cpp -o factorial.o                    
g++ -shared -W1,-soname,libfactorial.so -o libfactorial.so factorial.o
