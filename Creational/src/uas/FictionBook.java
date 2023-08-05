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
public class FictionBook implements Book {
    @Override
    public String getTitle() {
        // Implementasi judul buku fiksi
        return "Judul Buku Fiksi";
    }

    @Override
    public double getPrice() {
        // Implementasi harga buku fiksi
        return 50.0;
    }
}
