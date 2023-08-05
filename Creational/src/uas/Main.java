/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package uas;

/**
 *
 * @author muham
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
   
        // Factory Method Pattern
        String bookType = "fiction"; // Ganti dengan "nonfiction" untuk buku non-fiksi
        BookManagerFactory managerFactory;
        if (bookType.equals("fiction")) {
            managerFactory = new FictionBookManagerFactory();
        } else if (bookType.equals("nonfiction")) {
            managerFactory = new NonFictionBookManagerFactory();
        } else {
            throw new IllegalArgumentException("Jenis buku tidak valid.");
        }

        BookManager bookManager = managerFactory.createBookManager();
        bookManager.manageBook();

        // Abstract Factory Pattern
        Book book;
        Author author;
        bookType = "fiction"; // Ganti dengan "nonfiction" untuk buku non-fiksi
        if (bookType.equals("fiction")) {
            book = new FictionBook();
            author = new FictionAuthor();
        } else if (bookType.equals("nonfiction")) {
            book = new NonFictionBook();
            author = new NonFictionAuthor();
        } else {
            throw new IllegalArgumentException("Jenis buku tidak valid.");
        }
        System.out.println("Judul Buku: " + book.getTitle());
        System.out.println("Harga Buku: " + book.getPrice());
        System.out.println("Pengarang: " + author.getName());
        System.out.println("Biografi Pengarang: " + author.getBio());

        // Builder Pattern
        BookBuilder bookBuilder = new BookBuilder();
        bookBuilder.setTitle("Judul Buku");
        bookBuilder.setAuthor("Penulis Buku");
        bookBuilder.setPrice(100.00);
        bookBuilder.build();
    }
}
