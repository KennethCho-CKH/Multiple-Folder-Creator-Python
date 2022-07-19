/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace Multiple_Folder_Creator
{
    class Application
    {
        static void WelcomeText(){
            //Welcome text
            Console.WriteLine("Multiple Folder Creator");
            Console.WriteLine();
            Console.WriteLine("Created by KennethCho-CKH. Release under MPL 2.0 Licence.");
            Console.WriteLine();
            Console.WriteLine("Get the latest source code from GitHub! https://github.com/KennethCho-CKH/Multiple-Folder-Creator-CSharp");
            Console.WriteLine();
        }
        static void Main(string[] args)
        {
            WelcomeText();

            //Get path
            Console.WriteLine("Enter where you want your folder(s) to be created: ");
            string? FolderPath = Console.ReadLine();
            Console.WriteLine();

            //Get foldername
            Console.WriteLine("Enter the foldername you desired: ");
            string? input_FolderName = Console.ReadLine();
            Console.WriteLine();

            //Split the input string into list
            List<string> FolderName = input_FolderName!.Split(',').ToList();

            Console.WriteLine("Program Entered.");
            try
            {
                for (int ListNext = 0; ListNext < FolderName.Count; ListNext++)
                {
                    System.IO.Directory.CreateDirectory(FolderPath + FolderName[ListNext]);
                    Console.WriteLine("Program: " + FolderName[ListNext] + " created suscessfully.");
                }
            }
            //Error Handling
            catch (System.Exception)
            {
                Console.WriteLine("Program: Error: Folder(s) could not be created.");
                throw;
            }
            Console.WriteLine("Program: " + FolderName.Count.ToString() + " folders created suscessfully.");
            Console.WriteLine("Program Exited.");
        }
    }
}