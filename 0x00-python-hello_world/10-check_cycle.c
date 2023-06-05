#include "lists.h"

/**
 * check_cycle - Checks for a cycle in a linked list.
 * @list: The linked list to check.
 * Return: 1 if cycle exist, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t one = list;
	listint_t two = list;

	while (two && two->next)
	{
		one = one->next->next;
		two = two->next->next;

		if (one == two)
		{
			return (1);
		}
	}
	return (0);
}
