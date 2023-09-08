Dictionary<int, string> words = new Dictionary<int, string>() {[3] = "Fizz", [5] = "Buzz"};

for (int i = 1; i <= 100; i++)
{
    bool empty = true;
    foreach (var item in words)
    {
        if (i % item.Key == 0)
        {
            Console.Write(item.Value);
            empty = false;
        }
    }
    Console.WriteLine(empty ? i : "");
}