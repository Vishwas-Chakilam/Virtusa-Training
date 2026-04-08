import java.util.*;

class Book {
    private String id;
    private String title;
    private boolean isAvailable;

    public Book(String id, String title) {
        this.id = id;
        this.title = title;
        this.isAvailable = true;
    }
    
    public String getId() { return id; }
    public String getTitle() { return title; }
    public boolean getAvailability() { return isAvailable; }
    
    public void setAvailability(boolean status) { this.isAvailable = status; }

    @Override
    public String toString() {
        return "Book[ID=" + id + ", Title=" + title + ", Available=" + isAvailable + "]";
    }
}

class BookUnavailableException extends Exception {
    public BookUnavailableException(String msg) { super(msg); }
}

public class LibrarySystem {
    private List<Book> registry = new ArrayList<>();

    public void addBook(Book book) {
        registry.add(book);
        System.out.println("Added: " + book.getTitle());
    }

    public void borrowBook(String id) throws BookUnavailableException {
        for(Book b : registry) {
            if(b.getId().equals(id)) {
                if(b.getAvailability()) {
                    b.setAvailability(false);
                    System.out.println("Successfully borrowed: " + b.getTitle());
                    return;
                } else {
                    throw new BookUnavailableException(b.getTitle() + " is currently borrowed.");
                }
            }
        }
        System.out.println("Book not found in DB.");
    }

    public void displayBooks() {
        System.out.println("\n--- Library Catalog ---");
        registry.forEach(System.out::println);
        System.out.println("-----------------------\n");
    }

    public static void main(String[] args) {
        LibrarySystem lib = new LibrarySystem();
        lib.addBook(new Book("1", "Effective Java"));
        lib.addBook(new Book("2", "Clean Code"));
        
        lib.displayBooks();
        
        try {
            lib.borrowBook("1");
            lib.borrowBook("1"); // Should throw exception
        } catch (BookUnavailableException e) {
            System.err.println("Exception: " + e.getMessage());
        }
    }
}