class Factorial
{
    public:
        Factorial();
        long factorial(int);
};

Factorial::Factorial()
{}

long Factorial::factorial(int n)  
{  
  if (n == 0)  
    return 1;  
  else  
    return(n * factorial(n-1));  
} 

extern "C"
{
    Factorial* Factorial_new() { return new Factorial(); }
    int Factorial_factorial(Factorial* factorial, int n) {return factorial->factorial(n);}
}