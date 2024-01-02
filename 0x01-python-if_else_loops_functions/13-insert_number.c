#include "lists.h"

/**
 * insert_node - Write a function in C that inserts a
 * number into a sorted singly linked list.
 *
 * @head: A pointer
 *
 * @number: The number will be entered
 *
 * Return: the address of new node, NULL if failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p1;
	listint_t *p2;
	listint_t *p3;

	p2 = *head;
	p1 = malloc(sizeof(listint_t));

	if (p1 == NULL)
		return (NULL);

	while (p2 != NULL)
	{
		if (p2->n > number)
			break;
		p3 = p2;
		p2 = p2->next;
	}

	p1->n = number;

	if (*head == NULL)
	{
		p1->next = NULL;
		*head = p1;
	}
	else
	{
		p1->next = p2;
		if (p2 == *head)
			*head = p1;
		else
			p3->next = p1;
	}

	return (p1);
}
