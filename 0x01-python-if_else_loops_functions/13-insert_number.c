#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inset a number into a sorted singly linked list
 * @head: The head of sorted singly linked list
 * @number: The number to inserts in the singly linked list
 *
 * Return: The singly linked list with the new number added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list_current = NULL, *Newnodo = NULL, *temp = NULL;

	Newnodo = malloc(sizeof(listint_t));
	if (Newnodo == NULL)
		return (NULL);

	Newnodo->n = number;
	if (*head)
	{
		list_current = *head;
		if (number <= list_current->n)
		{
			Newnodo->next = list_current;
			*head = Newnodo;
		}
		else
		{
			while (list_current->next)
			{
				if (number <= list_current->next->n)
				{
					temp = list_current->next;
					list_current->next = Newnodo;
					Newnodo->next = temp;
					return (*head);
				}
				list_current = list_current->next;
			}
			temp = list_current->next;
			list_current->next = Newnodo;
			Newnodo->next = temp;
		}
		return (*head);
	}
	Newnodo->next = NULL;
	*head = Newnodo;
	return (*head);
}
