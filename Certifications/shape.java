// 1. Java: Shape
    
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Shape {
    protected int length;
    protected int breadth;
    
    public Shape(int length, int breadth) {
        this.length = length;
        this.breadth = breadth;
    }
    
    public void area() {
        System.out.println(length + " " + breadth);
    }
}

class Rectangle extends Shape {
    public Rectangle(int length, int breadth) {
        super(length, breadth);
    }
    
    @Override
    public void area() {
        int area = this.length * this.breadth;
        System.out.println(area);
    }
}

public class Solution {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        int b = sc.nextInt();

        Shape shape = new Shape(l,b);
        shape.area();

        Shape rectangle = new Rectangle(l,b);
        rectangle.area();
    }
}
