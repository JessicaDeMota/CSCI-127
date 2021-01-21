//Name:  Ranako Holder
//Email:  Ranako.holder15@myhunter.cuny.edu
//Date:  December 3, 2019

#include <iostream>
//using namespace std;

int main()
{
  int rows;
  int columns; 
  std::cout << "Enter the number of rows: ";
  std::cin >> rows;
  std::cout << std::endl << "Enter the number of columns: ";
  std::cin >> columns;
  std::cout << std::endl;

  for (int i = 0; i < rows; i++)
  {
    for (int j = 0; j < columns; j++)
    {
        if( (i + j) % 2 == 0 ){
            std::cout << "1";
        }
        else{
            std::cout << "0";
        }
            
    }
    std::cout << std::endl;
  }
  return 0;
}