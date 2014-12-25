#include <iostream> //Handles input/output operations (cout/cin)
#include <string> //Import the string class (mostly used within cin statements)
using namespace std;

void welcome(int caller);
void expression();

int main(){ 
	welcome(0);
	return 0;
}

void welcome(int caller){
	cout << "Welcome to iqMath!" << endl;
	cout << "What would you like to do?" << endl;
	cout << "1. Evaluate an expression." << endl;
	if (caller == 1)
		cout << "Please enter an integer that appears in the list above!" << endl;
	string response;
	cin >> response;
	if (response == "1") {
		expression();
	}
	else if (response == "2"){
		cout << "This is coming soon" << endl;
	}
	else {
		system("cls");
		welcome(1);
	}
}

void expression(){
	cout << "Enter the expression you would like to evaluate:" << endl;
	system("pause");
}