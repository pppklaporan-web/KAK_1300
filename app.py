import streamlit as st
from docxtpl import DocxTemplate
import io

st.set_page_config(page_title="Generator KAK BPS", layout="centered")

st.title("📄 Form Generator Kerangka Acuan Kerja (KAK)")
st.write("Formulir dokumen KAK Otomatis.")

# Form Input dari Pengguna
with st.form("form_kak"):
    st.subheader("1. Informasi Utama Kegiatan")
    col1, col2 = st.columns(2)
    with col1:
        judul = st.text_input("Judul Kegiatan", "FILTERISASI AIR SUMUR")
        kementerian = st.text_input("Kementerian/Lembaga", "Badan Pusat Statistik")
        unit_kerja = st.text_input("Unit Kerja", "BPS Provinsi Sumatera Barat")
    with col2:
        tim_kerja = st.text_input("Tim Kerja", "Tim Umum dan Keuangan")
        program = st.text_input("Program", "Program Penyediaan dan Pelayanan Informasi Statistik")
        kegiatan = st.text_input("Kegiatan", "Dukungan Manajemen dan Pelaksanaan Tugas Teknis Lainnya")

    st.subheader("2. Detail Anggaran & Akun")
    col3, col4 = st.columns(2)
    with col3:
        kelompok_ro = st.text_input("Kelompok Rincian Output", "Layanan Sarana dan Prasarana Internal")
        rincian_output = st.text_input("Rincian Output", "Layanan Pemeliharaan Perkantoran")
        komponen = st.text_input("Komponen", "Pemeliharaan Gedung dan Bangunan")
    with col4:
        akun = st.text_input("Akun", "523111")
        item_kegiatan = st.text_input("Item Kegiatan", "Pemeliharaan Filter Air")
        ppk = st.text_input("Nama Pejabat Pembuat Komitmen (PPK)", "Nama PPK, S.S.T., M.Si.")

    st.subheader("3. Uraian & Biaya")
    latar_belakang = st.text_area("Latar Belakang", "Air sumur di lingkungan kantor membutuhkan sistem filtrasi yang optimal...")
    maksud_tujuan = st.text_area("Maksud dan Tujuan", "Memastikan ketersediaan air bersih untuk operasional harian kantor.")
    target_sasaran = st.text_area("Target/Sasaran Kegiatan", "Terpeliharanya unit filter air secara berkala.")
    
    col5, col6 = st.columns(2)
    with col5:
        spdipa = st.text_input("No. SPDIPA", "DIPA-054.01.2.123456/2026")
        mak = st.text_input("MAK", "054.01.WA.2885.EBA.994.001.A.523111")
        detil = st.text_input("Detil Anggaran", "Pemeliharaan Filter Air Sumur Kantor BPS")
    with col6:
        rupiah = st.text_input("Total Biaya (Angka)", "15.000.000")
        bilangan = st.text_input("Terbilang (Huruf)", "Lima Belas Juta Rupiah")
        tgl_surat = st.text_input("Tanggal, Bulan, Tahun Penetapan", "19 Oktober 2026")

    spesifikasi_teknis = st.text_area("Spesifikasi Teknis", "1. Tabung Filter 10 Inci\n2. Media Carbon Active & Manganese")
    
    st.subheader("4. Penandatangan / Pejabat")
    col7, col8 = st.columns(2)
    with col7:
        ppl = st.text_input("Nama Pejabat Pembuat Komitmen (Di Bawah)", "Nama Pejabat Pembuat Komitmen")
        jabatan_kanan = st.text_input("Jabatan Penandatangan Kanan", "Kepala Bagian Umum atau Ketua TIM,")
    with col8:
        kabag = st.text_input("Nama Pejabat/Kabag/Ketua Tim (Kanan)", "Nama Kabag Umum, S.E., M.Si.")

    # Tombol Submit
    submit_button = st.form_submit_button(label="🚀 Generate Dokumen KAK")

if submit_button:
    try:
        # Load template Word
        doc = DocxTemplate("KAK Filterisasi Air Sumur.docx")
        
        # Mapping data form ke tag placeholder di Word
        context = {
            "JUDUL": judul,
            "Kementerian_Lembaga": kementerian,
            "Unit_Kerja": unit_kerja,
            "Tim_Kerja": tim_kerja,
            "Program": program,
            "Kegiatan": kegiatan,
            "Kelompok_Rincian_Output": kelompok_ro,
            "Rincian_Output": rincian_output,
            "Komponen": komponen,
            "Akun": akun,
            "Item_Kegiatan": item_kegiatan,
            "LATAR_BELAKANG": latar_belakang,
            "MAKSUD_DAN_TUJUAN": maksud_tujuan,
            "TARGET_SASARAN_KEGIATAN": target_sasaran,
            "PPK": ppk,
            "SPDIPA": spdipa,
            "MAK": mak,
            "Detil": detil,
            "Rupiah": rupiah,
            "Bilangan": bilangan,
            "Spesifikasi_Teknis": spesifikasi_teknis,
            "TGL_BULAN_TAHUN": tgl_surat,
            "PPL": ppl,
            "Jabatan_Kanan": jabatan_kanan,
            "KABAG": kabag
        }
        
        # Render dokumen
        doc.render(context)
        
        # Simpan ke memori buffer
        file_stream = io.BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)
        
        st.success("🎉 Dokumen KAK berhasil dibuat!")
        
        # Tombol Download
        st.download_button(
            label="📥 Download File Word (.docx)",
            data=file_stream,
            file_name=f"KAK_{judul}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
        
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

    st.divider()
st.markdown("<p style='text-align: center; color: gray;'>BPS 2026 - BPS SUMATERA BARAT</p>", unsafe_allow_html=True)
