#include <iostream>

using namespace std;

// Node structure for the linked list
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// LinkedList class
class LinkedList {
private:
    Node* head;

public:
    // Constructor
    LinkedList() : head(nullptr) {}

    // Function to insert a new node at the end of the linked list
    void insertNode(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = newNode;
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
        cout << "Node with value " << val << " inserted." << endl;
    }

    // Function to delete a node with a specific value from the linked list
    void deleteNode(int val) {
        if (head == nullptr) {
            cout << "Linked list is empty. Cannot delete." << endl;
            return;
        }

        if (head->data == val) {
            Node* temp = head;
            head = head->next;
            delete temp;
            cout << "Node with value " << val << " deleted." << endl;
            return;
        }

        Node* temp = head;
        while (temp->next != nullptr && temp->next->data != val) {
            temp = temp->next;
        }

        if (temp->next == nullptr) {
            cout << "Node with value " << val << " not found." << endl;
        } else {
            Node* toDelete = temp->next;
            temp->next = temp->next->next;
            delete toDelete;
            cout << "Node with value " << val << " deleted." << endl;
        }
    }

    // Function to search for a node with a specific value in the linked list
    void searchNode(int val) {
        Node* temp = head;
        int position = 1;

        while (temp != nullptr && temp->data != val) {
            temp = temp->next;
            position++;
        }

        if (temp == nullptr) {
            cout << "Node with value " << val << " not found." << endl;
        } else {
            cout << "Node with value " << val << " found at position " << position << "." << endl;
        }
    }
};

int main() {
    LinkedList linkedList;

    int choice;
    do {
        cout << "\nChoose operation:\n";
        cout << "1. Insertion\n";
        cout << "2. Deletion\n";
        cout << "3. Searching\n";
        cout << "0. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                int insertVal;
                cout << "Enter value to insert: ";
                cin >> insertVal;
                linkedList.insertNode(insertVal);
                break;

            case 2:
                int deleteVal;
                cout << "Enter value to delete: ";
                cin >> deleteVal;
                linkedList.deleteNode(deleteVal);
                break;

            case 3:
                int searchVal;
                cout << "Enter value to search: ";
                cin >> searchVal;
                linkedList.searchNode(searchVal);
                break;

            case 0:
                cout << "Exiting program.\n";
                break;

            default:
                cout << "Invalid choice. Please enter a valid choice.\n";
        }
    } while (choice != 0);

    return 0;
}
