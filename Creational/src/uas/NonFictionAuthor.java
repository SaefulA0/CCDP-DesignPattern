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
public class NonFictionAuthor implements Author {
    @Override
    public String getName() {
        // Implementasi nama pengarang buku non-fiksi
        return "Pengarang Buku Non-Fiksi";
    }

    @Override
    public String getBio() {
        // Implementasi biografi pengarang buku non-fiksi
        return "Biografi Pengarang Buku Non-Fiksi";
    }
}
