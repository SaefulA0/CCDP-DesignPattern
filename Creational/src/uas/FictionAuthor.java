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
public class FictionAuthor implements Author {
    @Override
    public String getName() {
        // Implementasi nama pengarang buku fiksi
        return "Pengarang Buku Fiksi";
    }

    @Override
    public String getBio() {
        // Implementasi biografi pengarang buku fiksi
        return "Biografi Pengarang Buku Fiksi";
    }
}
