using System;
using System.ComponentModel.Design.Serialization;
using System.Runtime.InteropServices;

class BiquadraticEquation
{
    protected double a;
    protected double b;
    protected double c;
    protected int num_roots;
    protected HashSet<double> roots = new HashSet<double>();

    public BiquadraticEquation(string[] coefs, double a = 0, double b = 0, double c = 0)
    {
        coef_setter(coefs, a, b, c);
    }
    protected void coef_setter(string[] coefs, double a, double b, double c)
    {
        if (coefs.Length == 0)
        {
            if (a == 0 && b == 0 && c == 0)
            {
                a_setter();
                b_setter();
                c_setter();
            } 
            else if (a == 0)
            {
                Console.WriteLine("А не может быть равно 0");
                a_setter();
                this.b = b;
                this.c = c;
            }
        } 
        else
        {
            if (double.TryParse(coefs[0], out double A))
            {
                if (A == 0)
                {
                    Console.WriteLine("А не может быть равно 0");
                    a_setter();
                }
                else
                {
                    this.a = A;
                }
            }
            else
            {
                Console.WriteLine("А введено не верно");
                a_setter();
            }
            if (double.TryParse(coefs[1], out double B))
            {
                this.b = B;
            }
            else
            {
                Console.WriteLine("B введено не верно");
                b_setter();
            }
            if (double.TryParse(coefs[2], out double C))
            {
                this.c = C;
            }
            else
            {
                Console.WriteLine("C введено не верно");
                c_setter();
            }
        }
    }
    protected void a_setter()
    {
        Console.WriteLine("Введите коэффициент A:");
        while (true) {
            if (double.TryParse(Console.ReadLine(), out double A))
            {
                a = A;
                break;
            } 
            else
            {
                Console.WriteLine("Не получается считать");
            }
        }
    }
    protected void b_setter()
    {
        Console.WriteLine("Введите коэффициент B:");
        while (true)
        {
            if (double.TryParse(Console.ReadLine(), out double B))
            {
                b = B;
                break;
            }
            else
            {
                Console.WriteLine("Не получается считать");
            }
        }
    }
    protected void c_setter()
    {
        Console.WriteLine("Введите коэффициент C:");
        while (true)
        {
            if (double.TryParse(Console.ReadLine(), out double C))
            {
                c = C;
                break;
            }
            else
            {
                Console.WriteLine("Не получается считать");
            }
        }
    }
    public void calculate_roots()
    {
        roots.Clear();
        num_roots = 0;
        double d = b * b - 4 * a * c;
        if (d == 0)
        {
            double t = (-1 * b) / (2 * a);
            if (t == 0)
            {
                roots.Add(0);
            }
            else if (t > 0)
            {
                roots.Add(Math.Sqrt(t));
                roots.Add(-1 * Math.Sqrt(t));
            }
        }
        else if (d > 0)
        {
            double t1 = (-1 * b + Math.Sqrt(d)) / (2 * a);
            double t2 = (-1 * b - Math.Sqrt(d)) / (2 * a);
            if (t1 == 0)
            {
                roots.Add(0);
            }
            else if (t1 > 0)
            {
                roots.Add(Math.Sqrt(t1));
                roots.Add(-1 * Math.Sqrt(t1));
            }
            if (t2 == 0)
            {
                roots.Add(0);
            }
            else if (t2 > 0)
            {
                roots.Add(Math.Sqrt(t2));
                roots.Add(-1 * Math.Sqrt(t2));
            }
        }
        num_roots = roots.Count;
    }
    public void roots_print()
    {
        if (num_roots == 0)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Нет корней");
            Console.ResetColor();
        }
        else
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Корни уравнения: ");
            foreach (var root in roots)
            {
                Console.Write($"{root.ToString()} ");
            }
            Console.Write("\n");
            Console.ResetColor();
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        BiquadraticEquation Equation = new BiquadraticEquation(args);
        Equation.calculate_roots();
        Equation.roots_print();
    }
}