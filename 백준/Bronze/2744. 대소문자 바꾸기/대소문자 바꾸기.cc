#include <iostream>
#include <string>

int main()
{
    std::string str;

    std::getline(std::cin, str);

    for (int i = 0; i < str.size(); i++) {
        if ('A' <= str[i] && str[i] <= 'Z') {
            str[i] += 32;
        }
        else if ('a' <= str[i] && str[i] <= 'z') {
            str[i] -= 32;
        }
    }
    std::cout << str << std::endl;

    return 0;
}