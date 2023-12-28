using System;

public abstract class GeometricFigure
{
    public abstract double CalculateArea();

    public abstract override string ToString();
}

public class Rectangle : GeometricFigure, IPrint
{
    public double Width { get; set; }
    public double Height { get; set; }

    public Rectangle(double width, double height)
    {
        Width = width;
        Height = height;
    }

    public override double CalculateArea()
    {
        return Width * Height;
    }

    public void Print()
    {
        Console.WriteLine(this.ToString());
    }

    public override string ToString()
    {
        return $"Ширина: {Width} Высота: {Height} Площадь: {CalculateArea()}";
    }
}

public class Square : Rectangle
{
    public Square(double side) : base(side, side) { }

    public new void Print()
    {
        Console.WriteLine(this.ToString());
    }

    public override string ToString()
    {
        return $"Сторона: {Height} Площадь: {CalculateArea()}";
    }
}

public class Circle : GeometricFigure, IPrint
{
    public double Radius { get; set; }

    public Circle(double radius)
    {
        Radius = radius;
    }

    public override double CalculateArea()
    {
        return Math.PI * Math.Pow(Radius, 2);
    }

    public void Print()
    {
        Console.WriteLine(this.ToString());
    }

    public override string ToString()
    {
        return $"Радиус: {Radius} Площадь: {CalculateArea()}";
    }
}

public interface IPrint
{
    void Print();
}

class Program
{
    static void Main()
    {
        Rectangle rectangle = new Rectangle(5, 10);
        Square square = new Square(4);
        Circle circle = new Circle(3);

        rectangle.Print();
        Console.WriteLine();

        square.Print();
        Console.WriteLine();

        circle.Print();
    }
}