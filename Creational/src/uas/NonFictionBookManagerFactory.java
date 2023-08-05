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
// NonFictionBookManagerFactory.java (Concrete Factory)
public class NonFictionBookManagerFactory implements BookManagerFactory {
    @Override
    public BookManager createBookManager() {
        return new NonFictionBookManager();
    }
}
