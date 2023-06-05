#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints all the elements of a listint_t list
 * @h: Pointer to the head node of the list
 * Return: Number of nodes in the list
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list
 * @head: Pointer to the head node of the list
 * @n: Integer value to be added to the new node
 * Return: Pointer to the new node
 */
listint_t *add_nodeint(listint_t **head, const int n);

/**
 * free_listint - Frees a listint_t list
 * @head: Pointer to the head node of the list
 */
void free_listint(listint_t *head);

/**
 * check_cycle - Checks if a linked list contains a cycle
 * @list: Pointer to the head node of the list
 * Return: 1 if a cycle is found, 0 otherwise
 */
int check_cycle(listint_t *list);

#endif /* LISTS_H */

