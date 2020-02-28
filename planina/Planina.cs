using System;

namespace planina_kattis
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int p = (int)Math.Pow(2, n) +1;
            Console.WriteLine(p*p);



        }
    }
}
