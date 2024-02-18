typedef struct Stack {
    char type;
    Stack* prev;
    Stack() : type('-'), prev(nullptr) {}
    Stack(char val) : type(val), prev(nullptr) {}
}* Node;
class Solution {
public:
    bool isValid(string s) {
        map<char, char> match = { {')','('},{'}','{' },{']','['} };
    Node top = new Stack(s[0]);
    for (int i = 1; i < s.length(); i++) {
        Node n = new Stack(s[i]);
        if (match[n->type] == top->type) {
            
            if (top->prev != nullptr) {
                Node holder = top->prev;
                delete top;
                top = holder;
            }
            else {
                delete top;
                top = nullptr;
            }
            if (top == nullptr)
                top = new Stack();
        }
        else if (top->type == '-') {
            top = n;
        }else {
            n->prev = top;
            top = n;
        }
    }
    return top->type == '-' ? true : false;
    }
};