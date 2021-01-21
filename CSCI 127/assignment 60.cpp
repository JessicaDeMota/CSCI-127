//Name:  Jessica De Mota Munoz 
//Email:  Jessica.DeMotaMunoz86@myhunter.cuny.edu
//Date:  December 3, 2019

#include <iostream>
using namespace std;

int main()
{
    int x,b;
    int numbers;
    std::cout << "Enter a number" ;
    std::cin >> numbers; 

    if (numbers < 0){
        cout << "1";
        x = numbers + 32;
    }
     else 
    {   
        cout << "0" ;
        x = numbers ;
    }
      b = 16;
      while (b >0.5){
          if (x >= b){
              cout << "1";
          }
          else 
          {
              cout << "0";
          }
            x = (x % b );
            b = (b / 2);
      }      
     cout << '\n';

}   
          
