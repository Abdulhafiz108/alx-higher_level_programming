#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - Inserts a number in a sorted singly linked list.
 * @head: A pointer to the head of the list
 * @number: Number to insert
 * Return: A pointer to new node and NUll on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *neew, *node;

	neew = malloc(sizeof(listint_t));
	if (!neew)
		return (NULL);

	neew->n = number;
	node = *head;
	if (node == NULL || node->n >= number)
	{
		neew->next = node;
		*head = neew;
		return (neew);
	}
	while (node)
	{
		if (node->next == NULL || node->next->n >= number)
		{
			neew->next = node->next;
			node->next = neew;
			return (neew);
		}
		node = node->next;
	}
	return (neew);
}
