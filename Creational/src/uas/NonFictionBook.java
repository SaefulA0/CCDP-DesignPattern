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
public class NonFictionBook implements Book {
    @Override
    public String getTitle() {
        // Implementasi judul buku non-fiksi
        return "Judul Buku Non-Fiksi";
    }

    @Override
    public double getPrice() {
        // Implementasi harga buku non-fiksi
        return 40.0;
    }
}
