#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: a pointer to a pointer to the head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head):
{
	if (head == NULL || *head == NULL)
		return (1);
	return (pal_check(head, *head));
}

/**
 * pal_check - trace list to check if it's palindrome or not
 *
 * @head: pointer to a pointer to the head
 *
 * @tracer: a pointer to trace with
 *
 * Return: 1 if true, 0 if false
*/

int pal_check(listint_t **head, listint_t *tracer)
{
	if (tracer == NULL)
		return (1);
	if (pal_check(head, tracer->next) && (*head)->n == tracer->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
