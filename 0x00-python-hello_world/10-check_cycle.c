 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *prob, *erob;

	if (list->next == NULL || list == NULL)
		return (0);

	prob = list->next;
	erob = list->next->next;

	while (erob && erob->next && prob)
	{
		if (prob == erob)
			return (1);

		prob = prob->next;
		erob = erob->next->next;
	}

	return (0);
}
