#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <conio.h>
#define TABLE_SIZE 10
struct node
{
	int Atomic_no;
	char symbol[5];
	char Element[30];
	float Atomic_mass;
	int group;
	char temp;
	struct node *next;
};

struct node *head[TABLE_SIZE] = {NULL}, *c;

void user_get(int Atomic_no, char symbol[], char Element[], float Atomic_mass, int group);
void insert(int Atomic_no, char symbol[], char Element[], float Atomic_mass, int group);
void delet();
void search();
void display();

int main()
{
	char symbol[5], Element[30], v[20];
	int Atomic_no, group, choice, i, n, l = 0;
	float Atomic_mass;
	insert(1, "H", "Hydrogen", 1.008, 1);
	insert(2, "He", "Helium", 4.003, 18);
	insert(3, "Li", "Lithium", 6.941, 1);
	insert(4, "Be", "Beryllium", 9.012, 2);
	insert(5, "B", "Boron", 10.811, 13);
	insert(6, "C", "Carbon", 12.011, 14);
	insert(7, "N", "Nitrogen", 14.007, 15);
	insert(8, "O", "Oxygen", 15.999, 16);
	insert(9, "F", "Fluorin", 18.998, 17);
	insert(10, "Ne", "Neon", 20.18, 18);
	insert(11, "Na", "Sodium", 22.99, 1);
	insert(12, "Mg", "Magnesium", 24.305, 2);
	insert(13, "Al", "Aluminium", 26.982, 13);
	insert(14, "Si", "Silicon", 28.086, 14);
	insert(15, "P", "Phosphorus", 30.974, 15);
	insert(16, "S", "Sulfur", 32.065, 16);
	insert(17, "Cl", "Chlorine", 35.453, 17);
	insert(18, "Ar", "Argon", 39.948, 18);
	insert(19, "K", "Potassium", 39.098, 1);
	insert(20, "Ca", "Calcium", 40.078, 2);
	insert(21, "Sc", "Scandium", 44.956, 3);
	insert(22, "Ti", "Titanium", 47.867, 4);
	insert(23, "V", "Vanadium", 50.942, 5);
	insert(24, "Cr", "Chromium", 51.996, 6);
	insert(25, "Mn", "Manganese", 54.938, 7);
	insert(26, "Fe", "Iron", 55.845, 8);
	insert(27, "Co", "Cobalt", 58.933, 9);
	insert(28, "Ni", "Nickel", 58.693, 10);
	insert(29, "Cu", "Copper", 63.546, 11);
	insert(30, "Zn", "Zinc", 65.39, 12);
	insert(31, "Ga", "Gallium", 69.723, 13);
	while (1)
	{

		printf("\n----------------------------------------------------------------\n\n");
		printf("\t\t1 Add new Element\n");
		printf("\t\t2 Delete Element\n");
		printf("\t\t3 Search Element details\n");
		printf("\t\t4 Display\n");
		printf("\t\t5 Exit \n");
		printf("\n----------------------------------------------------------------\n");
		printf("\n\t\tEnter your choice from above list   :  ");
		gets(v);
		l=0;
		do
		{
			if (!isdigit(v[l]))
			{
				printf("\n\t\t ERROR !!! ONLY POSITIVE INTEGER ARE ALLOW\n");
				printf("\n\t\tEnter your choice from above list   :  ");
				gets(v);
				l = 0;
			}
			else
				l++;
		} while (v[l] != '\0');
		choice = atoi(v);
		switch (choice)
		{
		case 1:
			user_get(Atomic_no, symbol, Element, Atomic_mass, group);
			break;
		case 2:
			delet();
			break;
		case 3:
			search();
			break;
		case 4:
			display();
			break;
		case 5:
			exit(0);
			break;
		default:
			printf("!!!!!!   ERROR  !!!!!!!!! Enter valid number ");
		}
	}
}

void user_get(int Atomic_no, char symbol[], char Element[], float Atomic_mass, int group)
{
	int l = 0, m = 0, n = 0, i, k;
	char v[20], a[20], b[20];
	struct node *newnode = (struct node *)malloc(sizeof(struct node));
label:
	fflush(stdin);
	printf("Enter a Atomic Number : ");
	gets(v);
	l = 0;
	do
	{
		if (!isdigit(v[l]))
		{
			printf("\n\t\t ERROR !!! ONLY POSITIVE INTEGER ARE ALLOW\n");
			printf("Enter a Atomic Number : ");
			gets(v);
			l = 0;
		}
		else
			l++;
	} while (v[l] != '\0');
	Atomic_no = atoi(v);
	k = Atomic_no;
	i = Atomic_no % TABLE_SIZE;
	if (head[i] == NULL)
	{
		printf("\nSearched element not found\n");
	}
	else
	{
		for (c = head[i]; c != NULL; c = c->next)
		{
			if (c->Atomic_no == k)
			{
				printf("\n!!!!!!!!!  This Atomic Number is Exist !!!!!!!!\n");
				goto label;
			}
		}
	}
	newnode->Atomic_no = Atomic_no;

	printf("Enter a symbol : ");
	gets(symbol);
	strcpy(newnode->symbol, symbol);

	printf("Enter Element full name : ");
	gets(Element);
	strcpy(newnode->Element, Element);

	printf("Enter Atomic Mass : ");
	scanf("%f", &Atomic_mass);
	newnode->Atomic_mass = Atomic_mass;
	fflush(stdin);

	printf("Enter the group of Element : ");
	gets(b);
	n=0;
	do
	{
		if (!isdigit(b[n]))
		{
			printf("\n\t\t ERROR !!! ONLY POSITIVE INTEGER ARE ALLOW\n");
			printf("Enter the group of Element : ");
			gets(b);
			n = 0;
		}
		else
			n++;
	} while (b[n] != '\0');
	group = atoi(b);
	newnode->group = group;

	if (head[i] == NULL)
	{
		head[i] = newnode;
	}
	else
	{
		c = head[i];
		while (c->next != NULL)
		{
			c = c->next;
		}
		c->next = newnode;
	}
}

void insert(int Atomic_no, char symbol[], char Element[], float Atomic_mass, int group)
{
	int i;
	i = Atomic_no % TABLE_SIZE;
	struct node *newnode = (struct node *)malloc(sizeof(struct node));
	newnode->Atomic_no = Atomic_no;
	strcpy(newnode->symbol, symbol);
	strcpy(newnode->Element, Element);
	newnode->Atomic_mass = Atomic_mass;
	newnode->group = group;
	newnode->next = NULL;
	if (head[i] == NULL)
	{
		head[i] = newnode;
	}
	else
	{
		c = head[i];
		while (c->next != NULL)
		{
			c = c->next;
		}
		c->next = newnode;
	}
}

void delet()
{
	
	struct node *temp1 = NULL, *follow = NULL;
	int l = 0, d_ele, i;
	char v[20];
	fflush(stdin);
	printf("Enter the Atomic number you want to delete : ");
	gets(v);
	l=0;
	do
	{
		if (!isdigit(v[l]))
		{
			printf("\n\t\t ERROR !!! ONLY POSITIVE INTEGER ARE ALLOW\n");
			printf("\nEnter the Atomic number you want to delete : ");
			gets(v);
			l = 0;
		}
		else
			l++;
	} while (v[l] != '\0');
	d_ele = atoi(v);
	i = d_ele % TABLE_SIZE;
	if (head[i] == NULL)
	{
		printf("\nElement not Exist\n");
	}
	else
	{
		temp1 = head[i];
		while (temp1 != NULL)
		{
			if (temp1->Atomic_no == d_ele)
			{
				follow->next = temp1->next;
				free(temp1);
				printf("\n%d deleted Successfully \n", d_ele);
				break;
			}
			else
			{
				follow = temp1;
				temp1 = temp1->next;
				if (follow->next == NULL)
				{
					printf("\nRecord Not Exist \n");
				}
			}
		}
	}
}
void search()
{
	int key, index, l = 0;
	char v[20];
	fflush(stdin);
	printf("Enter Atomic No for get properties : ");
	gets(v);
	l=0;
	do
	{
		if (!isdigit(v[l]))
		{
			printf("\n\t\t ERROR !!! ONLY POSITIVE INTEGER ARE ALLOW\n");
			printf("Enter Atomic No for get properties : ");
			gets(v);
			l = 0;
		}
		else
			l++;
	} while (v[l] != '\0');
	key = atoi(v);

	index = key % TABLE_SIZE;
	if (head[index] == NULL)
	{
		printf("\nSearched element not found\n");
	}
	else
	{
		for (c = head[index]; c != NULL; c = c->next)
		{
			if (c->Atomic_no == key)
			{
				printf("\n---------------------------------------------------------\n");
				printf("\t\t\tAtomic Number : %d\n\t\t\tSymbol : %s\n\t\t\tElement Name : %s\n\t\t\tAtomic mass : %.3f\n\t\t\tGroup : %d", c->Atomic_no, c->symbol, c->Element, c->Atomic_mass, c->group);
				printf("\n---------------------------------------------------------\n");
				break;
			}
		}
		if (c == NULL)

		{
			printf("\nSearched element not found\n");
		}
	}
}

void display()
{
	int key, l = 0;
	char v[20];
	fflush(stdin);
	printf("Enter index of 0 to 9  : ");
	gets(v);
	l=0;
	do
	{
		if (!isdigit(v[l]))
		{
			printf("\n\t\t ERROR !!! ONLY POSITIVE INTEGER ARE ALLOW\n");
			printf("Enter index of 0 to 9  : ");
			gets(v);
			l = 0;
		}
		else
			l++;
	} while (v[l] != '\0');
	key = atoi(v);
	if (key < 10 && key >= 0)
	{
		for (c = head[key]; c != NULL; c = c->next)
		{
			printf("\n---------------------------------------------------------\n");
			printf("\t\t\tAtomic Number : %d\n\t\t\tSymbol : %s\n\t\t\tElement Name : %s\n\t\t\tAtomic mass : %.3f\n\t\t\tGroup : %d", c->Atomic_no, c->symbol, c->Element, c->Atomic_mass, c->group);
			printf("\n---------------------------------------------------------\n");
		}
	}
	else
	{
		printf("\n!!!!!!!!!!!!!!!!!!!  Enter the index between 0 to 9!!!!!!!!!!! ");
	}
}
