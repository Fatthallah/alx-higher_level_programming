#include "lists.h"

/**
 * insert_node - The Fun Definition.
 * @ras: Refer To
 * @rakam: Refer To
 * Return: if error null or a new pointer
 */

listint_t *insert_node(listint_t **ras, int rakam)
{
	listint_t *node = *ras, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = rakam;

	if (node == NULL || node->n >= rakam)
	{
		new->next = node;
		*ras = new;
		return (new);
	}

	while (node && node->next && node->next->n < rakam)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
