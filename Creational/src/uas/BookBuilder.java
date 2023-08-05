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
public class BookBuilder {
    private String title;
    private String author;
    private double price;
    // Other book details, setters

    public void setTitle(String title) {
        this.title = title;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setPrice(double price) {
        this.price = price;
    }
    
    

    public BookProduct build() {
        BookProduct book = new BookProduct();
        book.setTitle(title);
        book.setAuthor(author); 
        book.setPrice(price);
        // Other book details, setters
        return book;
    }
}
