// #include <iostream>
// using namespace std;
// // g++ something.cpp -o main && ./main

// int main() {
//     // AN ACTUAL VALUE
//     // primative holds the value
//     int num = 42;
  
//     // A REFERENCE
//     // Points to the integer but cannot be reassigned 
//     int& ref = num;
    
//     // A POINTER
//     // Pointer to the integer
//     int* ptr = &num;

//     cout << "Value of the integer: " << num << endl;
//     cout << "Value of the pointer: " << ptr << endl;
//     cout << "Value of the reference: " << ref << endl;
//     cout << "Address of num: " << &num << endl;

//     return 0;
// }

#include <iostream>
using namespace std;

// Define a struct named Person
struct Person {
    string name;
    int age;
};

int main() {
    // Create an instance of the Person struct
    Person john;
    Person& johnRef = john; // this is what a reference looks like


    // Set the values for the data members
    john.name = "John Doe";
    john.age = 30;

    // Access and print the values
    cout << "Name: " << john.name << endl;
    cout << "Age: " << john.age << endl;

    return 0;
}
