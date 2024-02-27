#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Node allocation failed.\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;

    return newNode;
}

struct Node* appendToTail(struct Node* head, int data) {
    struct Node* newNode = createNode(data);

    struct Node* current = head;
    if (current == NULL) {
        return newNode;
    }

    while(current->next != NULL) {
        current = current->next;
    }

    current->next = newNode;
    return head;
}

void printLL(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d->", current->data);
        current = current->next;
    }
    printf("\n");
}

void freeLL(struct Node* head) {
    struct Node* current = head;
    struct Node* temp = NULL;

    while(current != NULL) {
        temp = current;
        current = current->next;
        printf("Free'd %d\n", temp->data);
        free(temp);
    }
}

int main(int argc, char** argv) {
    struct Node* head = NULL;

    if (head == NULL)
        printf("Head is NULL\n");
    else
        printf("Head is not NULL\n");


    for (int i = 0; i < 5; i++)
        head = appendToTail(head, i+1);    

    printLL(head);

    freeLL(head);

    printf("%d\n", head->data);

    if (head == NULL)
        printf("Head is NULL\n");
    else
        printf("Head is not NULL\n");

    return 0;
}