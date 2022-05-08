// https://scipy.github.io/old-wiki/pages/C%2B%2B_Extensions_that_use_NumPy_arrays.html
// https://www.auctoris.co.uk/2017/04/29/calling-c-classes-from-python-with-ctypes/

#include "ndarray.h"
#include <iostream>

class Runner{
    public:
        Runner()  { p = 0; };
        void setOutput(numpyArray<long> output);
        void print() { std::cout << p << std::endl; };
    
    private:
        int p;
        Ndarray<long,3>* output;
};


void Runner::setOutput(numpyArray<long> output) {
    Ndarray<long,3> a(output);

    std::cout << a.getShape(0) << " " << a.getShape(1) << " " << a.getShape(2) << std::endl;
    this->output = &a;
    std::cout << &a << std::endl;
}

//Ndarray<int,3> Runner::getOutput() {
//    return this->output;
//};

extern "C"
{
    Runner* Runner_new() { return new Runner(); }
    void Runner_setOutput(Runner* runner, numpyArray<long> output) { return runner->setOutput(output);}
    void Runner_print(Runner* runner) { return runner->print(); };
//    Ndarray<int,3> Runner_getOutput(Runner* runner) { return runner->getOutput();}
}