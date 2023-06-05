#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: Singly linked list node structure
 * for Holberton project.
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints all the elements of a listint_t list.
 * @h: Pointer to the head node.
 * Return: Number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list.
 * @head: Pointer to the pointer of the head node.
 * @n: Value to set in the new node.
 * Return: Pointer to the new node or NULL on failure.
 */
listint_t *add_nodeint(listint_t **head, const int n);

/**
 * free_listint - Frees a listint_t list.
 * @head: Pointer to the head node.
 */
void free_listint(listint_t *head);

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @list: Pointer to the head of the list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list);

#endif /* LISTS_H */

