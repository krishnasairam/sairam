package com.techmojo.roka;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller // This means that this class is a Controller
@RequestMapping(path="/demo") // This means URL's start with /demo (after Application path)
public class MainController {
	@Autowired
    UserService service;
 
    @RequestMapping
    public String getAllEmployees(Model model) 
    {
        List<User> list = service.getAllUsers();
 
        model.addAttribute("users", list);
        return "list-employees";
    }
 
    @RequestMapping(path = {"/edit", "/edit/{id}"})
    public String editEmployeeById(Model model, @PathVariable("id") Optional<Long> id) 
                            throws RecordNotFoundException 
    {
        if (id.isPresent()) {
            User entity = service.getUserById(id.get());
            model.addAttribute("user", entity);
        } else {
            model.addAttribute("user", new User());
        }
        return "add-edit-employee";
    }
     
    @RequestMapping(path = "/delete/{id}")
    public String deleteEmployeeById(Model model, @PathVariable("id") Long id) 
                            throws RecordNotFoundException 
    {
        service.deleteUserById(id);
        return "redirect:/demo";
    }
 
    @RequestMapping(path = "/createUser", method = RequestMethod.POST)
    public String createOrUpdateEmployee(User user) 
    {
        service.createOrUpdateUser(user);
        return "redirect:/demo";
    }
	
}








//@Autowired // This means to get the bean called userRepository
//// Which is auto-generated by Spring, we will use it to handle the data
//private UserRepository userRepository;
//@Autowired
//private AccountsRepository accountsRepository;
//
//@PostMapping(path="/add") // Map ONLY POST Requests
//public @ResponseBody String addNewUser (@RequestParam String name
//, @RequestParam String email, @RequestParam Long mobile
//, @RequestParam String address) {
//// @ResponseBody means the returned String is the response, not a view name
//// @RequestParam means it is a parameter from the GET or POST request
//
//User n = new User();
//n.setName(name);
//n.setEmail(email);
//n.setMobile(mobile);
//n.setAddress(address);
//userRepository.save(n);
//return "Saved";
//}
//
//@GetMapping(path="/allusers")
//public @ResponseBody Iterable<User> getAllUsers() {
//// This returns a JSON or XML with the users
//return userRepository.findAll();
//}
//
//@GetMapping(path="/deleteallusers")
//public @ResponseBody String deleteall() {
//userRepository.deleteAll();
//return "deleted";
//}
//
//@PostMapping(path="/deleteuser")
//public @ResponseBody String delete(@RequestParam Long mobile) {
//userRepository.deleteById(mobile);
//return "deleted";
//}
//
//@PostMapping(path="/addamount") // Map ONLY POST Requests
//public @ResponseBody String addToAccount (@RequestParam Long mobile
//, @RequestParam Integer account, @RequestParam Integer wallet) {
//// @ResponseBody means the returned String is the response, not a view name
//// @RequestParam means it is a parameter from the GET or POST request
//
//UserAccounts a = new UserAccounts();
//a.setMobile(mobile);
//a.setAccount(account);
//a.setWallet(wallet);
//accountsRepository.save(a);
//return "Saved";
//}
//
//@GetMapping(path="/allaccounts")
//public @ResponseBody Iterable<UserAccounts> getAllAccounts() {
//// This returns a JSON or XML with the users
//return accountsRepository.findAll();
//}
//
//@GetMapping(path="/deleteallaccounts")
//public @ResponseBody String deleteallaccounts() {
//accountsRepository.deleteAll();
//return "deleted";
//}
//
//@PostMapping(path="/deleteaccount")
//public @ResponseBody String deleteaccount(@RequestParam Long mobile) {
//accountsRepository.deleteById(mobile);
//return "deleted";
//}
//