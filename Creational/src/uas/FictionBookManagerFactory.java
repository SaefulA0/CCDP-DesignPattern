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
// FictionBookManagerFactory.java (Concrete Factory)
public class FictionBookManagerFactory implements BookManagerFactory {
    @Override
    public BookManager createBookManager() {
        return new FictionBookManager();
    }
}
