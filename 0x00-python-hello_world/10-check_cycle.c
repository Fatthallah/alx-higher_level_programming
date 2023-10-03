#include "lists.h"

/**
 * check_cycle - This Fun Checks The Cycle.
 * @list: Refer To The L.L To Be Checked.
 * Return: When Cycle 1 or 0 If not
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	if (!list)
		return (0);

	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}

	return (0);
}
