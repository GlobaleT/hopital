from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from.models import Doctor,Patient,Appointment
from .models import Medicament
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .models import Facture, Patient

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    if not request.user.is_staff:
        return redirect('admin_login')  # Correction : renvoie vers 'admin_login' et non 'login'
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    medicament = Medicament.objects.all()
    d=0
    p=0
    a=0
    m=0
    for i in doctors:
        d+=1
    for i in patient:
        p+=1    
    for i in appointment:
        a+=1     
    for i in medicament:
        m+=1      
    d1={'d':d,'p':p,'a':a,'m':m}     
        
    return render(request, 'index.html',d1)

def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST.get('uname')  # Utilisation de .get() pour éviter KeyError
        p = request.POST.get('pwd')
        user = authenticate(username=u, password=p)

        if user is not None and user.is_staff:
            auth_login(request, user)  # Utilisation correcte de login()
            return redirect('dashboard')  # Redirection vers la page d'accueil après connexion
        else:
            error = "yes"  # Affiche le message d'erreur

    return render(request, 'login.html', {'error': error})

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('admin_login')  # Correction : redirection correcte
    logout(request)
    return redirect('admin_login')


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html',d)  # ⛔ Mauvaise syntaxe


def Add_Doctor(request):
    error = ""
    success = False
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST.get('name')
        m = request.POST.get('mobile')
        e = request.POST.get('email')
        sp = request.POST.get('specialite')
        ad = request.POST.get('adresse')

        try:
            Doctor.objects.create(name=n, mobile=m, email=e, specialite=sp, adresse=ad)
            success = True  # ✅ Ajout réussi
        except:
            error = "yes"

    return render(request, 'add_doctor.html', {'error': error, 'success': success})

            

       


def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id =pid)
    doctor.delete()
    
    return redirect('view_doctor')  # ⛔ Mauvaise syntaxe






def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pt = Patient.objects.all()
    p = {'pt':pt}
    return render(request, 'view_patient.html',p)  # ⛔ Mauvaise syntaxe


def Add_Patient(request):
    error = ""
    success = False
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST.get('name')
        dt = request.POST.get('date_naissance ')
        m = request.POST.get('mobile ')
        gd = request.POST.get('gender ')
        ad = request.POST.get('adresse')

        try:
            Patient.objects.create(name=n, date_naissance=dt, mobile=m, gender=gd, adresse=ad)
            success = True  # ✅ Ajout réussi
        except:
            error = "yes"

    return render(request, 'add_patient.html', {'error': error, 'success': success})

            

       


def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id =pid)
    patient.delete()
    
    return redirect('view_patient')  # ⛔ Mauvaise syntaxe





def view_medicament(request):
    """ Vue pour afficher tous les médicaments en pharmacie """
    medicaments = Medicament.objects.all()
    return render(request, 'view_medicament.html', {'medicaments': medicaments})


def Add_Medicament(request):
    error = ""
    success = False
    
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST.get('nom')
        d = request.POST.get('description')
        c = request.POST.get('categorie')
        qt = request.POST.get('quantite_stock')
        p = request.POST.get('prix')
        dt = request.POST.get('date_expiration')  # ✅ Correction ici

        try:
            Medicament.objects.create(
                nom=n, 
                description=d, 
                categorie=c, 
                quantite_stock=qt, 
                prix=p, 
                date_expiration=dt  # ✅ Correction ici
            )
            success = True  # ✅ Ajout réussi
        except:
            error = "yes"

    return render(request, 'add_medicament.html', {'error': error, 'success': success})  # ✅ Correction ici






def Update_medicament(request, pid):
    medicament = get_object_or_404(Medicament, id=pid)

    if request.method == 'POST':
        # Récupérer les données envoyées par le formulaire
        medicament.nom = request.POST.get('nom')  
        medicament.categorie = request.POST.get('categorie')
        medicament.quantite_stock = request.POST.get('quantite_stock')
        medicament.prix = request.POST.get('prix')
        medicament.date_expiration = request.POST.get('date_expiration')

        # Validation des champs obligatoires (par exemple, "nom" et "quantite_stock")
        if not medicament.nom or not medicament.quantite_stock:
            error_message = "Le nom et la quantité en stock sont obligatoires."
            return render(request, 'update_medicament.html', {'medicament': medicament, 'error_message': error_message})

        # Sauvegarder les modifications
        medicament.save()

        # Rediriger après la mise à jour
        return redirect('view_medicament',)

    return render(request, 'update_medicament.html', {'medicament': medicament})





def Delete_Medicament(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    medicamet = Medicament.objects.get(id =pid)
    medicamet.delete()
    
    return redirect('view_medicament')  # ⛔ Mauvaise syntaxe







def Add_Patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date_naissance = request.POST.get('date_naissance')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        adresse = request.POST.get('adresse')
        

        if name and mobile:  # Ajoute des vérifications de validation
            Patient.objects.create(
                name=name,
                mobile=mobile,
                gender=gender,
                adresse=adresse,
                date_naissance=date_naissance
            )
            messages.success(request, "Le patient a été ajouté avec succès !")
            return redirect('view_patient')
        else:
            messages.error(request, "Erreur : veuillez remplir tous les champs requis.")

    return render(request, 'add_patient.html')




def Add_Appointment(request):
    error = ""
    success = False
    if not request.user.is_staff:
        return redirect('login')
    
    doc = Doctor.objects.all()
    pt = Patient.objects.all()
    
    if request.method == "POST":
        doctor_id = request.POST.get('doctor')  # Récupérer l'ID au lieu du nom
        patient_id = request.POST.get('patient')
        dt = request.POST.get('date')
        t = request.POST.get('time')
        
        doctor = Doctor.objects.filter(id=doctor_id).first()  # 🔹 Correction ici
        patient = Patient.objects.filter(id=patient_id).first()

        if doctor and patient:
            try:
                Appointment.objects.create(doctor=doctor, patient=patient, date=dt, time=t)
                success = True
                return redirect('view_appointment')  # Rediriger après succès
            except Exception as e:
                error = "yes"
                print(f"Erreur lors de l'ajout du rendez-vous : {e}")  # Debugging
        else:
            error = "yes"  # Si le docteur ou le patient est introuvable

    return render(request, 'add_appointment.html', {'doc': doc, 'pt': pt, 'error': error, 'success': success})


from django.core.paginator import Paginator

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    
    appointments = Appointment.objects.all().order_by('-date')  # Trier par date décroissante
    
    # Pagination
    paginator = Paginator(appointments, 10)  # 10 rendez-vous par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'appointments': page_obj}  # 🔹 Correction ici (avant c'était 'doc')
    return render(request, 'view_appointment.html', context)





def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.get(id =pid)
    app.delete()
    
    return redirect('view_appointment')  # ⛔ Mauvaise syntaxe






def Add_Facture(request):
    error = ""
    success = False
    if not request.user.is_staff:
        return redirect('login')
    
    patients = Patient.objects.all()  # Récupérer tous les patients
    
    if request.method == "POST":
        p_id = request.POST.get('patient')  # Récupérer l'ID du patient
        m = request.POST.get('montant_total')
        desc = request.POST.get('description')

        patient = Patient.objects.filter(id=p_id).first()  # Vérifier si le patient existe

        if patient:
            try:
                Facture.objects.create(patient=patient, montant_total=m, description=desc)
                success = True  # ✅ Ajout réussi
            except Exception as e:
                error = "yes"
                print(e)  # Debugging

    return render(request, 'add_facture.html', {'patients': patients, 'error': error, 'success': success})
