#include "lists.h"

/**
 * check_cycle - Checks for a cycle in a linked list.
 * @list: The linked list to check.
 * Return: 1 if cycle exist, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *one = list;
	listint_t *two;

	while (one->next)
	{
		two = one->next;

		while (two)
		{
			if (two->next == one)
			{
				return (1);
			}
			two = two->next;
		}
		one = one->next;
	}
	return (0);
}
